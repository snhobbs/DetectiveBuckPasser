from setuptools import setup, find_packages
setup(name='buckPasser',
		version='0.0.0b7',
		description='Detective Buck Passer',
		url='http://github.com/snhobbs/DetectiveBuckPasser',
		author='Simon Hobbs & Joey Ricci',
		author_email='simon.hobbs@hobbs-eo.com',
		license='BSD',
		packages=find_packages(),
		install_requires=[
			'pyfiglet',
			'click',
			'colorama',
			'miniboa',
            'pexpect'
		],
                scripts=["bin/runServer.sh"]
		test_suite='nose.collector',
		tests_require=['nose'],
		include_package_data=True,
		zip_safe=True)
