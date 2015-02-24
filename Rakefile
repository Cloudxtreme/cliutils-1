#
#
#
#FUNCTIONS 
#
#
#Return the file list to be installed
def file_list()

	files = FileList[
		'kde/*',
		'media/*',
		'system/*',
		'utils/*'
 	]
 	return files
end

#Return de list of aliases to add in the rc file
def aliases()
	aliases=[]
	aliases << 'alias upgrade="aptitude update;aptitude -y safe-upgrade;aptitude clean"'
	aliases << 'alias updateutils=""'
end

#If rake has been run without sudo, try to rerun the task with it
def sudo(task)
		puts "sudo"
		system("sudo rake #{task}")
end

#
#
#TASKS
#
#
desc "Install cliutils"
task :install do# {{{

	#TODO: Add aliases to rc files
	#TODO: Deploy instead install?
	files = file_list()

	puts "Installing..."

    begin
		files.each do |file|
			dest =  File.join("/usr/local/bin/", File.basename(file)) 
			ln_s(File.expand_path(file), dest) if File.exists?(file) unless File.exists?(dest)
		end
		
	rescue
		sudo(:install)
	end

end# }}}

desc "Uninstall cliutils "
task :uninstall do# {{{
	puts "Uninstalling..."
	files=file_list()
	
	begin

		files.each do |file|
			installed=File.join("/usr/local/bin/",File.basename(file))
			rm installed 
		end

	rescue
    	sudo(:uninstall)
	end
end# }}}

task :default => :install
# task :default do
# 	system 'rake -T'
# end
