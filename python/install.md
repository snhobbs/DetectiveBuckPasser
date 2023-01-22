<h2>Windows Install:</h2>
	Doesn't work as well on Windows. This is Microsoft's fault.
	<h3>1) Get Python3</h3>	
		<a>https://www.howtogeek.com/197947/how-to-install-python-on-windows/</a>
		<ul>
		<li>Add python3.6.1 or higher</li>
		</ul>
	<h3>2) Download Code</h3>
			<ul>
			<li>Download the zip file <a>https://github.com/snhobbs/DetectiveBuckPasser/archive/master.zip</a></li>
			<li>Unzip the code</li>
			<li>cd into the python36 directory enter the Scripts directory</li>
			<li>Install the requirements with pip install -r winrequirements.txt</li>
			<li>Open a command window in the directory that has buckPasser.py</li></ul>	
	<h3>Running</h3>
			<ul>
			<li>Type: py buckPasser.py</li>
			</ul>	

<h2>Linux/BSD/Mac/Solaris/AIX Install:</h2>
	<h3>You almost already have python3!</h3>
	<h3>Clone the repository or download the zip</h3>
		<ul>
		<li>Download the zip file <a>https://github.com/snhobbs/DetectiveBuckPasser/archive/master.zip</a></li>
		<li>Unzip and ensure your working directory is the one with buckPasser.py</li>
		<li>Get the requirements by running pip install -r requirements.txt (Make sure you are using the correct pip for your python3)</li>
		</ul>
	<h3>Running</h3>
		<ul><li>Type: python3 buckPasser.py or just ./buckPasser.py</li></ul>

<h2>Dependancies for Sound</h2>
Sound is not functional unless the simpleaudio package is installed, but the game runs fine without it. Windows and the Unixs support it.
