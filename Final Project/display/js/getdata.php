<?php
	function getLastPageLink($url){
		$file = file_get_contents($url);

		$temp = explode('last": {"href": "', $file);
		$lastpage = explode('", "title": "last page"', $temp[1]);
		$lastpagelink = 'http://192.168.137.199:5000/'.$lastpage[0];
		return $lastpagelink;
	}

	
	$link_bmp = getLastPageLink('http://192.168.137.199:5000/bmpTable');
	$link_tsl = getLastPageLink('http://192.168.137.199:5000/tslTable');
	$link_dht = getLastPageLink('http://192.168.137.199:5000/dhtTable');

	//Latest data
	//TSL raw
	$lastpage = file_get_contents($link_tsl);
	$id_tsl = explode('_id', $lastpage);
	$latest_tsl_data = $id_tsl[count($id_tsl)-2];
	//BMP raw
	$lastpage = file_get_contents($link_bmp);
	$id_bmp = explode('_id', $lastpage);
	$latest_bmp_data = $id_bmp[count($id_bmp)-2];
	//DHT raw
	$lastpage = file_get_contents($link_dht);
	$id_dht = explode('_id', $lastpage);
	$latest_dht_data = $id_dht[count($id_dht)-2];

	//TSL data
	$tsl_full_luminosity = explode('full_luminosity": ', $latest_tsl_data);
	$tsl_full_luminosity = explode(', "lux":',$tsl_full_luminosity[1]);
	$tsl_full_luminosity = $tsl_full_luminosity[0];

	$tsl_lux = explode('"lux": ', $latest_tsl_data);
	$tsl_lux = explode(', "_links"',$tsl_lux[1]);
	$tsl_lux = $tsl_lux[0];

	$tsl_ir_luminosity = explode('"ir_luminosity": ', $latest_tsl_data);
	$tsl_ir_luminosity = explode(', "', $tsl_ir_luminosity[1]);
	$tsl_ir_luminosity = $tsl_ir_luminosity[0];

	//BMP data
	$bmp_temperature = explode('"temperature": ', $latest_bmp_data);
	$bmp_temperature = explode(', "altitude"',$bmp_temperature[1]);
	$bmp_temperature = $bmp_temperature[0];

	$bmp_altitude = explode('"altitude": ', $latest_bmp_data);
	$bmp_altitude = explode(', "pressure"',$bmp_altitude[1]);
	$bmp_altitude = $bmp_altitude[0];

	$bmp_pressure = explode('"pressure": ', $latest_bmp_data);
	$bmp_pressure = explode(', "sea_level_pressure"',$bmp_pressure[1]);
	$bmp_pressure = $bmp_pressure[0];

	$bmp_sea_level_pressure = explode('"sea_level_pressure": ', $latest_bmp_data);
	$bmp_sea_level_pressure = explode(', "_links"',$bmp_sea_level_pressure[1]);
	$bmp_sea_level_pressure = $bmp_sea_level_pressure[0];

	//DHT
	$dht_temperature = explode('"temperature": ', $latest_dht_data);
	$dht_temperature = explode(', "humidity"',$dht_temperature[1]);
	$dht_temperature = $dht_temperature[0];

	$dht_humidity = explode('"humidity": ', $latest_dht_data);
	$dht_humidity = explode(', "_links"',$dht_humidity[1]);
	$dht_humidity = $dht_humidity[0];

	$datalist = array(
		'tsl_full_luminosity' => $tsl_full_luminosity,
		'tsl_lux' => $tsl_lux,
		'tsl_ir_luminosity' => $tsl_ir_luminosity,
		'bmp_temperature' => $bmp_temperature,
		'bmp_altitude' => $bmp_altitude,
		'bmp_pressure' => $bmp_pressure,
		'bmp_sea_level_pressure' => $bmp_sea_level_pressure,
		'dht_temperature' => $dht_temperature,
		'dht_humidity' => $dht_humidity
		);

	echo json_encode($datalist);	
?>