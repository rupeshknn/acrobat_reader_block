ForEach ($path in Get-Content "E:\New folder\Adobe_Blocklist.txt") #path to blocklist
{
	$file = $path.Split("\")[-1]
	$rule = New-NetFirewallRule -DisplayName $file.ToString() -Direction Outbound -Action Block -Program $path.ToString() -Profile Any;
	$rule.Group = "Adobe block";
	$rule | Set-NetFirewallRule;
}

	
