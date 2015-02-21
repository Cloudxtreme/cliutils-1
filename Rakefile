def file_list()

	files = FileList[
		'kde/*',
		'media/*',
		'system/*',
		'utils/*'
 	]
 	return files
end

def sudo(task)
	begin
		system("sudo rake #{task}")
	rescue
		puts "Aborted"
	end
end

desc "Install cliutils"
task :install do

	files = file_list()

	puts "Installing..."

	files.each do |file|
		puts File.basename(file, ".py")
		puts file
		puts
	end

end

desc "Uninstall cliutils "
task :uninstall do
	files=file_list()
	
	begin

		files.each do |file|
			installed="/usr/local/bin/"+File.basename(file)
			rm installed
		end

	rescue
    	sudo(:uninstall)
	end
end

task :default => :install
# task :default do
# 	system 'rake -T'
# end
