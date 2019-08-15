项目基于django2.2+sqlit+tengine2.1.2

tengine 安装
patch -p1 < ../ngx_req_status/write_filter.patch

./configure --with-http_upstream_check_module --user=www-data --group=www-data --prefix=/etc/nginx --sbin-path=/usr/sbin --error-log-path=/var/log/nginx/error.log --conf-path=/etc/nginx/nginx.conf --pid-path=/run/nginx.pid --add-module=../ngx_req_status



