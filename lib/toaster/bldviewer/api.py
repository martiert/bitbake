#
# BitBake Toaster Implementation
#
# Copyright (C) 2013        Intel Corporation
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

from django.conf.urls import patterns, include, url


urlpatterns = patterns('bldviewer.views',
        url(r'^builds$', 'model_explorer',  {'model_name':'build'}, name='builds'),
        url(r'^targets$', 'model_explorer',  {'model_name':'target'}, name='targets'),
        url(r'^tasks$', 'model_explorer', {'model_name':'task'}, name='task'),
        url(r'^task_dependencies$', 'model_explorer',  {'model_name':'task_dependency'}, name='task_dependencies'),
        url(r'^packages$', 'model_explorer',  {'model_name':'build_package'}, name='build_packages'),
        url(r'^package_dependencies$', 'model_explorer',  {'model_name':'build_package_dependency'}, name='build_package_dependencies'),
        url(r'^target_packages$', 'model_explorer',  {'model_name':'target_package'}, name='target_packages'),
        url(r'^package_files$', 'model_explorer',  {'model_name':'build_file'}, name='build_files'),
        url(r'^layers$', 'model_explorer', {'model_name':'layer'}, name='layer'),
        url(r'^layerversions$', 'model_explorer', {'model_name':'layerversion'}, name='layerversion'),
        url(r'^recipes$', 'model_explorer', {'model_name':'recipe'}, name='recipe'),
        url(r'^recipe_dependencies$', 'model_explorer',  {'model_name':'recipe_dependency'}, name='recipe_dependencies'),
        url(r'^variables$', 'model_explorer',  {'model_name':'variable'}, name='variables'),
        url(r'^logmessages$', 'model_explorer',  {'model_name':'logmessage'}, name='logmessages'),
)
