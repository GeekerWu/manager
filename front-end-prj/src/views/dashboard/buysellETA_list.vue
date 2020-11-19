<template>
    <a-card :bordered="false" class="content">
        <img id="new" src="../../assets/icons/new_status.png" height="0" width="25"/>
        <img id="change" src="../../assets/icons/change_status.png" height="0" width="25"/>
        <div class="table-page-search-wrapper">
            <a-form layout="inline" @submit="handleSubmit" :form="form">
                <a-row :gutter="48">
                    <a-col :md="6" :sm="24" v-for="item in filterList.slice(0,1)" :key="item.index">
                        <a-form-item :label="item.label">
                            <a-input
                                    :placeholder="item.placeHolder"
                                    v-if="item.inputType=='input'"
                                    :disabled="item.editDisabled"
                                    v-decorator="[item.decorator, {rules: [{required: item.required, message: item.message }]}]"
                            />
                            <a-select
                                    showSearch
                                    :getPopupContainer="getPopupContainer"
                                    :filterOption="filterOption"
                                    optionFilterProp="children"
                                    v-if="item.inputType=='dropDown'"
                                    :placeholder="item.placeHolder"
                                    mode="multiple"
                                    :allowClear="item.allowClear"
                                    v-decorator="[item.decorator, {rules: [{required: item.required, message: item.message }]}]"
                                    @change="handleDropDownChange($event, item.decorator)"
                            >
                                <!--mode="multiple"-->
                                <a-select-option
                                        v-for="(element, i) in item.dropDownList"
                                        :key="i"
                                        :value="element"
                                >{{ element }}
                                </a-select-option>
                            </a-select>

                            <a-date-picker
                                    v-if="item.inputType=='date'"
                                    :getCalendarContainer="getPopupContainer"
                                    :disabled="item.editDisabled"
                                    :placeholder="item.placeHolder"
                                    :allowClear="item.allowClear"
                                    v-decorator="[item.decorator, {rules: [{required: item.required, message: item.message }]}]"
                            />
                            <a-auto-complete
                                                  v-if="item.inputType=='autoComplete'"
                                                   :disabled="item.editDisabled"
                                                  :placeholder="item.message"
                                                   :allowClear="item.allowClear"
                                                  v-decorator="[item.decorator,{rules:[{required:item.required,message:item.message}]}]"
                                                   @change="handleDropDownChange($event,item.decorator)"
                            >
                                <template slot="dataSource">
                                    <a-select-option v-for="option in item.autoDropDownList" :key="option">{{ option
                                        }}
                                    </a-select-option>
                                </template>
                            </a-auto-complete>
                        </a-form-item>
                    </a-col>
                    <a-col :md="6" :sm="24" v-for="item in filterList.slice(1,2)" :key="item.index">
                        <a-form-item :label="item.label">
                            <a-input
                                    :placeholder="item.placeHolder"
                                    v-if="item.inputType=='input'"
                                    :disabled="item.editDisabled"
                                    v-decorator="[item.decorator, {rules: [{required: item.required, message: item.message }]}]"
                            />
                            <a-select
                                    showSearch
                                    :getPopupContainer="getPopupContainer"
                                    :filterOption="filterOption"
                                    optionFilterProp="children"
                                    v-if="item.inputType=='dropDown'"
                                    :placeholder="item.placeHolder"
                                    mode="multiple"
                                    :allowClear="item.allowClear"
                                    v-decorator="[item.decorator, {rules: [{required: item.required, message: item.message }]}]"
                                    @change="handleDropDownChange($event, item.decorator)"
                            >
                                <a-select-option
                                        v-for="(element, i) in item.dropDownList"
                                        :key="i"
                                        :value="element"
                                >{{ element }}
                                </a-select-option>
                            </a-select>
                            <!-- mode="multiple"-->
                            <a-date-picker
                                    v-if="item.inputType=='date'"
                                    :getCalendarContainer="getPopupContainer"
                                    :disabled="item.editDisabled"
                                    :placeholder="item.placeHolder"
                                    :allowClear="item.allowClear"
                                    v-decorator="[item.decorator, {rules: [{required: item.required, message: item.message }]}]"
                            />
                            <a-auto-complete
                                                                        v-if="item.inputType=='autoComplete'"
                                                                        :disabled="item.editDisabled"
                                                                        :placeholder="item.message"
                                                                        :allowClear="item.allowClear"
                                                                        v-decorator="[item.decorator, { rules: [{required: item.required, message: item.message }]}]"
                                                                        @change="handleDropDownChange($event, item.decorator)"
                                                                >
                                <template slot="dataSource">
                                    <a-select-option v-for="option in item.autoDropDownList" :key="option">{{ option
                                        }}
                                    </a-select-option>
                                </template>
                            </a-auto-complete>
                        </a-form-item>
                    </a-col>
                    <a-col :md="6" :sm="24" v-for="item in filterList.slice(2,3)" :key="item.index">
                        <a-form-item :label="item.label">
                            <a-input
                                    :placeholder="item.placeHolder"
                                    v-if="item.inputType=='input'"
                                    :disabled="item.editDisabled"
                                    v-decorator="[item.decorator, {rules: [{required: item.required, message: item.message }]}]"
                            />
                            <a-select
                                    showSearch
                                    :getPopupContainer="getPopupContainer"
                                    :filterOption="filterOption"
                                    optionFilterProp="children"
                                    v-if="item.inputType=='dropDown'"
                                    mode="multiple"
                                    :placeholder="item.placeHolder"
                                    :allowClear="item.allowClear"
                                    v-decorator="[item.decorator, {rules: [{required: item.required, message: item.message }]}]"
                                    @change="handleDropDownChange($event, item.decorator)"
                                    @keyup.enter.native="getItemNo($event)"
                                    @search="searchValue"
                            >
                                <a-select-option
                                        v-for="(element, i) in item.dropDownList"
                                        :key="i"
                                        :value="element"
                                >{{ element }}
                                </a-select-option>
                            </a-select>
                            <a-date-picker
                                    v-if="item.inputType=='date'"
                                    :getCalendarContainer="getPopupContainer"
                                    :disabled="item.editDisabled"
                                    :placeholder="item.placeHolder"
                                    :allowClear="item.allowClear"
                                    v-decorator="[item.decorator, {rules: [{required: item.required, message: item.message }]}]"
                            />
                        </a-form-item>
                    </a-col>
                    <a-col :md="6" :sm="24" v-for="item in filterList.slice(3,4)" :key="item.index">
                        <a-form-item :label="item.label">
                            <a-input
                                    :placeholder="item.placeHolder"
                                    v-if="item.inputType=='input'"
                                    :disabled="item.editDisabled"
                                    v-decorator="[item.decorator, {rules: [{required: item.required, message: item.message }]}]"
                            />
                            <a-select
                                    showSearch
                                    :getPopupContainer="getPopupContainer"
                                    :filterOption="filterOption"
                                    optionFilterProp="children"
                                    v-if="item.inputType=='dropDown'"
                                    mode="multiple"
                                    :placeholder="item.placeHolder"
                                    :allowClear="item.allowClear"
                                    v-decorator="[item.decorator, {rules: [{required: item.required, message: item.message }]}]"
                                    @change="handleDropDownChange($event, item.decorator)"
                            >
                                <a-select-option
                                        v-for="(element, i) in item.dropDownList"
                                        :key="i"
                                        :value="element"
                                >{{ element }}
                                </a-select-option>
                            </a-select>
                            <a-date-picker
                                    v-if="item.inputType=='date'"
                                    :getCalendarContainer="getPopupContainer"
                                    :disabled="item.editDisabled"
                                    :placeholder="item.placeHolder"
                                    :allowClear="item.allowClear"
                                    v-decorator="[item.decorator, {rules: [{required: item.required, message: item.message }]}]"
                            />
                        </a-form-item>
                    </a-col>

                </a-row>
                <a-row :gutter="48">
                    <a-col :md="6" :sm="24" v-for="item in filterList.slice(4,5)" :key="item.index">
                        <a-form-item :label="item.label">
                            <a-input
                                    :placeholder="item.placeHolder"
                                    v-if="item.inputType=='input'"
                                    :disabled="item.editDisabled"
                                    v-decorator="[item.decorator, {rules: [{required: item.required, message: item.message }]}]"
                            />
                            <a-date-picker
                                    v-if="item.inputType=='date'"
                                    :getCalendarContainer="getPopupContainer"
                                    :disabled="item.editDisabled"
                                    :placeholder="item.placeHolder"
                                    :allowClear="item.allowClear"
                                    v-decorator="[item.decorator, {rules: [{required: item.required, message: item.message }]}]"
                            />
                        </a-form-item>
                    </a-col>

                    <a-col :md="12" :sm="24">

                    </a-col>
                    <a-col :md="6" :sm="24">
            <span
                    class="table-page-search-customButtons"
                    style="float: right">
              <a-button
                      type="primary"
                      style="margin-left: 8px;margin-top: 2px"
                      :disabled="this.editable"
                      :size="size"
                      :loading="searchLoading"
                      @click="SearchOnClick()"
              >Search</a-button>
              <a-button
                      type="primary"
                      style="margin-left: 8px;margin-top: 2px"
                      icon="download"
                      :size="size"

                      :disabled="searchLoading||this.editable"

                      @click="onBtExport"
              >{{ $t('lang.tabComAgExportButtonName') }}</a-button>
            </span>
                    </a-col>
                </a-row>
                <a-divider style="margin-top: 0px;margin-bottom: 10px; height: 5px;"/>
                <a-row :gutter="24" style="margin-top: 15px;">
                    <a-col :md="16" :sm="24">
            <span
                    class="table-page-search-customButtons"
                    v-if="this.userAuth=='ADMIN'||this.userAuth=='GSM'||this.userAuth=='SUPPLIER'"
            >
              <a-button
                      type="primary"
                      v-if="this.userAuth=='ADMIN'||this.userAuth=='GSM'||this.userAuth=='SUPPLIER'"
                      style="margin-left: 8px;margin-top: 2px"
                      icon="form"
                      :size="size"
                      :disabled="searchLoading||this.editable||this.weekly||this.monthly"
                      @click="onBtEdit()"
              >{{ $t('lang.tabComEditComponentTitle') }}</a-button>
              <a-button
                      type="primary"
                      v-if="this.userAuth=='ADMIN'||this.userAuth=='GSM'||this.userAuth=='SUPPLIER'"
                      style="margin-left: 8px;margin-top: 2px"
                      icon="upload"
                      :size="size"
                      :disabled="searchLoading||this.editable"
                      @click="uploadOnClick"
              >{{ $t('lang.tabComUpload') }}</a-button>
              <a-button
                      type="primary"
                      :size="size"
                      v-if="this.userAuth=='ADMIN'||this.userAuth=='GSM'"
                      style="margin-left: 8px;margin-top: 2px"
                      :disabled="searchLoading||this.submitBtn=='show'||this.editable" @click="PublishBPSClick">
                <img
                        v-if="!searchLoading&&this.submitBtn!='show'&&!this.editable"
                        src="../../assets/icons/publish.png" height="15" width="15"/>
                                <img v-if="searchLoading||this.submitBtn=='show'||this.editable"
                                     src="../../assets/icons/publish_loading.png" height="15" width="15"/>

                <span style="margin-left: 6px;">publish BPS</span>
              </a-button>
              <a-button
                      type="primary"
                      :size="size"
                      v-if="this.userAuth=='ADMIN'||this.userAuth=='GSM'"
                      style="margin-left: 8px;margin-top: 2px"
                      :disabled="searchLoading||this.submitBtn=='show'||this.editable" @click="PublishETAClick">
                <img
                        v-if="!searchLoading&&this.submitBtn!='show'&&!this.editable"
                        src="../../assets/icons/publish.png"
                        height="15"
                        width="15"/>
                <img
                        v-if="searchLoading||this.submitBtn=='show'||this.editable"
                        src="../../assets/icons/publish_loading.png"
                        height="15"
                        width="15"/>

                <span style="margin-left: 6px;">publish ETA</span>
              </a-button>



            </span>
                    </a-col>
                    <a-col :md="8" :sm="24">
                     <span
                             class="table-page-search-customButtons"
                             style="float: right; margin-left: 8px;margin-top: 2px"
                     >

                          <a-button v-if="this.editable" type="primary"
                                    style="margin-left: 8px;margin-top: 2px" :size="size" @click="SubmitOnClick">
                                {{ $t('lang.addCommonSubmit') }}</a-button>
                         <!--type="danger"-->
                            <a-button v-if="this.editable" type="dashed"
                                      style="margin-left: 8px;margin-top: 2px" :size="size" @click="CancelOnClick">
                {{ $t('lang.addCommonCancel') }}</a-button>

              <img v-if="!searchLoading&&!this.weekly&&!this.editable" src="../../assets/icons/weekly_loading.png"
                   height="25" width="25" @click="weeklyclick()"/>
              <img v-if="!searchLoading&&this.weekly&&!this.editable" src="../../assets/icons/weekly.png" height="25"
                   width="25" @click="weeklyclick()"/>

              <img v-if="!searchLoading&&!this.monthly&&!this.editable" src="../../assets/icons/monthly_loading.png"
                   height="25" width="25" @click="monthlyclick()"/>
              <img v-if="!searchLoading&&this.monthly&&!this.editable" src="../../assets/icons/monthly.png" height="25"
                   width="25" @click="monthlyclick()"/>

            </span>
                    </a-col>
                </a-row>
            </a-form>
        </div>
        <br/>
        <!-- :sideBar="sideBar"-->
        <ag-grid-vue :style="agStyle" class="ag-theme-balham"
                     :gridOptions="gridOptions"
                     :sideBar="sideBar"
                     :statusBar="statusBar"
                     @grid-ready="onGridReady"
                     :columnDefs="columnDefs"
                     :defaultColDef="defaultColDef"
                     :autoGroupColumnDef="autoGroupColumnDef"
                     :rowGroupPanelShow="rowGroupPanelShow"
                     :suppressAggFuncInHeader="suppressAggFuncInHeader"
                     :suppressRowClickSelection="true"
                     :purgeClosedRowNodes="purgeClosedRowNodes"
                     :getChildCount="getChildCount"
                     :pivotPanelShow="pivotPanelShow"
                     :rowData="rowData"
                     :animateRows="true"
                     :modules="modules"
                     :rowSelection="rowSelection"
                     :suppressDragLeaveHidesColumns="suppressDragLeaveHidesColumns"
                     :suppressMakeColumnVisibleAfterUnGroup="suppressMakeColumnVisibleAfterUnGroup"
                     :groupDefaultExpanded="groupDefaultExpanded"
                     :frameworkComponents="frameworkComponents"
                     :loadingOverlayComponent="loadingOverlayComponent"
                     :loadingOverlayComponentParams="loadingOverlayComponentParams"
                     :noRowsOverlayComponent="noRowsOverlayComponent"
                     :noRowsOverlayComponentParams="noRowsOverlayComponentParams"
                     :enableRangeSelection="true"
                     :suppressRowTransform="true"
                     multiSortKey="ctrl"
                     @cellEditingStarted="cellEditingStarted"
                     @cellValueChanged="onCellValueChanged"
                     :stopEditingWhenGridLosesFocus="true"
                     :singleClickEdit="true"
                     :isRowSelectable="isRowSelectable"
                     :undoRedoCellEditing="true"
                     :undoRedoCellEditingLimit="5"
                     :enableCellChangeFlash="true"
                     @row-selected="onRowSelected"
        >
        </ag-grid-vue>

        <br/>
        <a-form>
            <a-row :gutter="48">
                <a-col :md="8" :sm="24">

                </a-col>

                <a-col :md="16" :sm="24">
          <span style="float:right;margin-right: 1px;">
            <a-pagination
                    show-quick-jumper
                    show-size-changer
                    v-model="current"
                    :total="total"
                    :page-size="pageSize"
                    :page-size-options="pageSizeOptions"
                    @showSizeChange="onShowSizeChange"
                    @change="pagechange"
                    :show-total="total => `Total ${total} items`"
            />
          </span>
                </a-col>
                <a-col :md="8" :sm="24">

                </a-col>

            </a-row>
        </a-form>

    </a-card>
</template>

<script>
    /* eslint-disable camelcase */
    /* eslint-disable eqeqeq */
    import Vue from 'vue'
    import moment from 'moment'
    import {hasSearchFilters, getNoRowOverlayMsg} from '@api/sdcUtil'
    import {tableBtns} from '@/components'
    import {
        data,
        columndef,
        rowdata_normal,
        filterList,
        getDropDownList,
        getITEMNo,
        getDateMapping,
        ETAstyleList,
        ETAdynamicUpdate,
        shortagePublish,
        etaPublish
    } from '@api/wuqitest_api'
    import footbar from './footbar.js'
    import statusrender from './statusrender'
    //    import langZh from '../../locales/zh-CN/partsOwner_lang.js';
    //    import langEn from '../../locales/en-US/partsOwner_lang.js';
    import CustomNoRowsOverlay from '../../components/Overlay/customNoRowsOverlay.js'
    import CustomLoadingOverlay from '../../components/Overlay/customLoadingOverlay.js'
    import {isNullOrUndefined} from 'util'
    import {AgGridVue} from '@ag-grid-community/vue'
    import {AllModules} from '@ag-grid-enterprise/all-modules'
    import ACol from 'ant-design-vue/es/grid/Col'
    import {exportByURL} from '@api/exportFunction_api'
    import {NumberUtil } from '@/utils/NumberUtil.js'

    export default {
        name: 'TableList',
        components: {
            ACol,
            AgGridVue,
            tableBtns
        },
        data() {
            return {
                ITEM: '',
                userAuth: '',
                ItemListData: [],

                size: 'default',
                editBtn: 'show',
                addBtn: 'show',
                submitBtn: 'hide',
                EditRowIndex: null,
                currentDate: null,

                querysupplier: null,

                //                highlightList:[],
                monthendday: [],
                weekendday: [],
                weekday: [],
                monthday: [],
                dayhide: false,
                weekhide: true,
                columnGroupShow: 'open',
                monthhide: true,
                editable: false,
                changelist: [],
                uploadId: 'UPLOAD_BS_ORDERSHORTAGE',
                user_role: 'Supplier', // GSM ,Supplier,ODM
                spanchangedata: [],

                DatetoDay: [],
                spancolumn: [],
                spanrowdata: [],
                cellDefs: null,

                statusBar: null,

                ETAItemList: [],
                ETAsiteIdList: [],
                ETABUList: [],
                ETASupplierList: [],

                weekly: false,
                monthly: false,
                pageSizeOptions: ['50', '100', '500', '1000'],
                current: 1,
                pageSize: 1000,
                total: null,

                // support agGrid
                agStyle: null,
                gridOptions: null,
                columnDefs: [],
                rowData: null,
                gridApi: null,
                columnApi: null,
                rowCount: null,
                defaultColDef: null,
                autoGroupColumnDef: null,
                rowGroupPanelShow: null,
                getChildCount: null,
                GroupPanelShow: null,
                pivotPanelShow: null,
                suppressAggFuncInHeader: null,
                purgeClosedRowNodes: null,
                suppressDragLeaveHidesColumns: null,
                suppressMakeColumnVisibleAfterUnGroup: null,
                groupDefaultExpanded: null,
                export_name: 'buysellETA',
                frameworkComponents: null,
                loadingOverlayComponent: null,
                loadingOverlayComponentParams: null,
                noRowsOverlayComponent: null,
                noRowsOverlayComponentParams: null,
                isRowSelectable: null,
                modules: AllModules,
                rowSelection: 'multiple',
                editType: 'fullRow',
                brandDataList: [],
                OwnerSiteIdList: [],
                filterList: [],
                //                filterList: langEn.filter_langEn,
                //                filterList: this.$store.getters.language == 'en_US' ? langEn.filter_langEn : langZh.filter_langZh,
                form: this.$form.createForm(this),
                currentPageManipulationAuth: ['Add', 'Delete', 'Update', 'View', 'Upload', 'Export'],
                mdl: {},
                searchLoading: false,
                loading: false, // 页面是否加载中
                advanced: false, // 高级搜索 展开/关闭
                queryParam: {}, // 查询参数
                optionAlertShow: true, // 是否显示选择框
                selectedRowKeys: [], // 选中的行的keys数组
                selectedRows: [], // 选中的行的全部数组
                // 表头
                columns: [],
                loadData: '',
                options: {
                    alert: {
                        show: true,
                        clear: () => {
                            this.selectedRowKeys = []
                        }
                    },
                    rowSelection: {
                        selectedRowKeys: this.selectedRowKeys,
                        onChange: this.onSelectChange
                    },
                    customRow: {
                        click: this.aaaa
                    }
                }
            }
        },
        activated() {
            if (Vue.ls.get('odmETA_closed')) {
                Vue.ls.set('odmETA_closed', false)
                this.form.resetFields()
            }

            if (Vue.ls.get('odmETA_closed')) {
                Vue.ls.set('odmETA_closed', false)
                Vue.ls.set(
                    'noRowsOverlayMsg_ID',
                    getNoRowOverlayMsg('init', this.language)
                )
                this.queryParam = {}
                this.filtersChange = !this.filtersChange
                this.form.resetFields()
            }
        },
        beforeMount() {
            this.gridOptions = {}
            this.defaultColDef = {
                width: 130,
                allowedAggFuncs: ['sum', 'min', 'max'],
                sortable: true,
                resizable: true,
                enablePivot: true,
                filter: true,
                floatingFilter: true
            }
            this.initbucket()
            this.sideBar = {
                toolPanels: [
                    {
                        id: 'columns',
                        labelDefault: 'Columns',
                        labelKey: 'columns',
                        iconKey: 'columns',
                        toolPanel: 'agColumnsToolPanel',
                        toolPanelParams: {
                            suppressPivots: true,
                            suppressPivotMode: true
                        }
                    }
                ],
                // pivot
                defaultToolPanel: 'columns'
            }

            this.autoGroupColumnDef = {width: 180}

            this.suppressDragLeaveHidesColumns = 'true'
            this.getChildCount = data => {
                return Math.round(Math.random() * 100 + 1)
            }
            // overlay
            this.frameworkComponents = {
                customLoadingOverlay: CustomLoadingOverlay,
                customNoRowsOverlay: CustomNoRowsOverlay,
                footbar: footbar,
                statusrender: statusrender

            }
            this.loadingOverlayComponent = 'customLoadingOverlay'
            this.loadingOverlayComponentParams = {
                loadingMessageFunc() {
                    return 'Loading ...'
                }
            }
            this.noRowsOverlayComponent = 'customNoRowsOverlay'
            this.noRowsOverlayComponentParams = {
                noRowsMessageFunc() {
                    return 'there is no data'
                }
            }
            // selectable
            this.isRowSelectable = rowNode => {
                return rowNode.data ? (rowNode.data.status !== 'complete' && rowNode.data.status !== 'resent complete') : false
            }

            this.statusBar = {

                statusPanels: [

                    {
                        statusPanel: 'agAggregationComponent',
                        align: 'right',
                        statusPanelParams: {
                            aggFuncs: ['count', 'sum', 'min', 'max', 'avg']
                        }
                    }
                ]

            }
        },
        mounted() {
            this.gridApi = this.gridOptions.api
            this.gridColumnApi = this.gridOptions.columnApi
            this.getItemNo()
        },
        computed: {
            language() {
                return this.$store.getters.language
            },
            openedMenuItem() {
                return this.$store.getters.openedMenuItem
            }
        },
        created() {
            window.addEventListener('resize', this.getHeight)
            this.getHeight()
            this.changeLanguage()
            this.getDropDown(
                {moduleName: 'getETAItemList'},
                this.ETAItemList,
                'ITEM'
            )
            this.getDropDown(
                {moduleName: 'getETAsiteIdList'},
                this.ETAsiteIdList,
                'SITEID'
            )
            this.getDropDown(
                {moduleName: 'getETABUList'},
                this.ETABUList,
                'BU'
            )
            this.getDropDown(
                {moduleName: 'getETASupplierList'},
                this.ETASupplierList,
                'SUPPLIERID'
            )

            this.setDropDownLists()
        },
        watch: {
            openedMenuItem: {
                handler(val) {
                    if (!isNullOrUndefined(val) &&
                        val.path.startsWith('buysellETA/buysellETA_list')) {
                        // setfilter
                        const savedFilterReports = JSON.parse(
                            localStorage.getItem('savedFilterReports')
                        )
                        const filterName = this.openedMenuItem.name
                        const path = this.openedMenuItem.path
                        if (
                            savedFilterReports[filterName] &&
                            this.$route.path == '/' + path.split('?query=')[0]
                        ) {
                            this.form.resetFields()
                            this.queryParam = JSON.parse(
                                decodeURI(savedFilterReports[filterName])
                            )
                            setTimeout(() => {
                                const temp = JSON.parse(decodeURI(savedFilterReports[filterName]))
                                for (const key in temp) {
                                    this.form.setFieldsValue({[key]: temp[key]})
                                }
                            }, 500)
                            this.customize()
                        } else {
                            this.form.resetFields()
                        }
                        ;
                    }
                },
                immediate: true
            },

            columnGroupShow() {
            },

            searchLoading() {
                if (this.searchLoading) {
                    // show 'loading' overlay
                    this.gridApi.showLoadingOverlay()
                }
            },

            ETAItemList(val) {
                this.filterList.forEach(element => {
                    if (element['decorator'] == 'item') {
                        /* console.log('this.ETAItemList',this.ETAItemList); */
                        element['dropDownList'] = [].concat(this.ETAItemList)
                    }
                })
            },
            ETAsiteIdList(val) {
                this.filterList.forEach(element => {
                    if (element['decorator'] == 'siteid') {
                        element['dropDownList'] = [].concat(this.ETAsiteIdList)
                    }
                })
            },
            ETABUList(val) {
                this.filterList.forEach(element => {
                    if (element['decorator'] == 'bu') {
                        element['dropDownList'] = [].concat(this.ETABUList)
                    }
                })
            },
            ETASupplierList(val) {
                this.filterList.forEach(element => {
                    if (element['decorator'] == 'supplier') {
                        element['dropDownList'] = [].concat(this.ETASupplierList)
                    }
                })
            },

            language(val) {
                this.changeLanguage()
            },
            '$route': {
                handler(route) {
                },
                deep: true
            }

        },

        methods: {
            onBtEdit() {
                this.spanchangedata = []
                this.editable = !this.editable
                this.weekly = false
                this.monthly = false
                this.columnGroupShow = 'closed',
                    this.weekhide = false
                this.monthhide = false
                this.columnDefs = []
                this.changeLanguage()
            },
            handleChange(value) {
            },
            searchValue(value) {
                this.ITEM = value
            },

            getItemNo(e) {
                const params = {
                    moduleName: 'getETAItemList',
                    ITEM: this.ITEM
                }
                getITEMNo(params)
                    .then(res => {
                        if (res.code == 0) {
                            var itemlist = []
                            res.result.forEach(item => {
                                itemlist.push(item.ITEM)
                            })
                            this.ETAItemList = itemlist
                        }
                    })
            },

            monthlyclick() {
                this.monthly = !this.monthly
                if (this.weekly) {
                    this.weekly = false
                }

                if (this.monthly) {
                    //                    this.columnGroupShow='open',
                    this.columnGroupShow = 'open',
                        this.dayhide = true
                    this.weekhide = true
                    this.monthhide = false
                    this.columnDefs = []
                    this.changeLanguage()
                } else if (this.weekly == false && this.monthly == false) {
                    this.columnGroupShow = 'closed',
                        this.dayhide = false
                    this.weekhide = true
                    this.monthhide = true
                    this.columnDefs = []
                    this.changeLanguage()
                }
            },

            weeklyclick() {
                this.weekly = !this.weekly
                if (this.monthly) {
                    this.monthly = false
                }

                if (this.weekly) {
                    this.columnGroupShow = 'open'
                    this.dayhide = false
                    this.weekhide = false
                    this.monthhide = true
                    this.columnDefs = []
                    this.changeLanguage()
                    console.log(this.columnDefs)

                } else if (this.weekly == false && this.monthly == false) {
                    this.columnGroupShow = 'closed'
                    this.dayhide = false
                    this.weekhide = true
                    this.monthhide = true
                    this.columnDefs = []
                    this.changeLanguage()
                }
            },

            MissPartonChange() {
                console.log('missing part change')
            },

            onShowSizeChange(current, size) {
                console.log('current is:', current, '   pagesize is:', size)
                this.pageSize = size
                this.current = 1
                this.customize()
            },
            pagechange(page, pageSize) {
                console.log('curr Page: ', page, 'pagesize is:', pageSize)
                this.pageSize = pageSize
                this.current = page
                this.customize()
            },
            SearchOnClick() {
                this.current = 1
                this.customize()
            },

            customize() {
                console.log('customize');
                /***
                 * 调用接口，从数据库查询数据方法
                 * paramters :
                 *  1.pageNum 页数
                 *      不分页，所以设置pageNum:1
                 *  2.pageSize 每页数据量
                 *      ag-grid使用的是假分页，但可以支持100000数据加载到内存，所以设置pageSize:100000
                 */
                const that = this;
                this.searchLoading = true;
                this.form.validateFields((err, values) => {
                    if (!err) {
                        let supplier = []
                        if (values.supplier != undefined) {
                            supplier = values.supplier
                        } else supplier = this.querysupplier;

                        this.queryParam.uiName = "ODM_SHORTAGE";
                        this.queryParam.pageNum = this.current;
                        this.queryParam.pageSize = this.pageSize;
                        this.queryParam.ITEM = values.item;
                        this.queryParam.SITEID = values.siteid;
                        this.queryParam.BU = values.bu;
                        this.queryParam.PROCITEMGROUP = values.procitemgroup;
                        this.queryParam.SUPPLIERID = supplier;

                    } else {
                        const message = 'Search condition error'
                        const description = 'please input search conditions'
                        that.$message.error(that.$Utils.messageWithClose(message, description))
                    }
                })
                rowdata_normal(this.queryParam)
                    .then(res => {
                        // 刷新 Ag-grid dataset
                        that.rowData = res.result.list
                        that.total = res.result.total
                        that.spancolumn = res.result.cells.colunms
                        that.spanrowdata = res.result.cells.grps
                        that.searchLoading = false
                        this.changeLanguage()
                        return res
                    }).catch(err => {
                    console.log(err)
                })
                // autosize
                var allColumnIds = []
                this.gridColumnApi.getAllColumns().forEach(function (column) {
                    allColumnIds.push(column.colId)
                })
                setTimeout(this.gridColumnApi.autoSizeColumns(allColumnIds, true), 2000)

            },
            onGridReady() {
                if (!this.searchLoading) {
                    this.gridApi.showNoRowsOverlay()
                }
            },
            onRowSelected(event) { // agtable 选择列表
                this.selectedRowKeys = []
                for (let i = 0; i < this.gridApi.getSelectedRows().length; i++) {
                    this.selectedRowKeys.push(this.gridApi.getSelectedRows()[i].rid)
                }
            },
            getPopupContainer(trigger) {
                return trigger.parentElement
            },
            uploadOnClick() {
                const originalPage = this.$route.name
                this.$router.replace({
                    path: `/upload/upload_list/${this.uploadId}/origin/${originalPage}`
                })
            },
            //todo 此方法应该按照 type判断
            onCellValueChanged(params) {
                var that = this
                console.log('onCellValueChanged:', params, params.data.RID)
                var changeindex = this.changelist.findIndex(item => item.RID == params.data.RID)
                if (changeindex >= 0) {
                    this.changelist[changeindex] = params.data
                } else {
                    this.changelist.push(params.data)
                }
                if (params.colDef.rowSpan) {
                    var editcolname = params.colDef.field
                    var count = this.spanrowdata.filter(item => item.rid == params.data.RID)[0].count
                    var startindex = this.rowData.findIndex(item => item.RID == params.data.RID)
                    var spandata = this.rowData.slice(startindex, parseInt(startindex) + parseInt(count))
                    spandata.forEach(item => {
                        var editcolname2 = params.colDef.field
                        console.log(item.RID)
                        var push_item =
                            {
                                'RID': item.RID,
                            }
                        push_item[editcolname] = params.value
                        this.spanchangedata.push(push_item)
                    })
                    console.log(this.spanchangedata)
                }

                if (params.colDef.field == 'SHIPPINGSCHEDULE') {
                    // 100@2020-10-01,120@2020-10-02,120@2020-10-05,
                    var haserror = false;
                    var strlength = params.data.SHIPPINGSCHEDULE.length
                    var lastApha = params.data.SHIPPINGSCHEDULE.slice(strlength - 1)
                    console.log('shipping str:', params.data.SHIPPINGSCHEDULE, 'length:', strlength, 'last lastApha:', lastApha)
                    if (lastApha != ',') {
                        params.value = params.value + ','
                    }
                    var changelist = []
                    var newstr = params.value
                    while (newstr.indexOf(',') > 0) {
                        var dataindex = newstr.indexOf(',')
                        var curr = newstr.slice(0, dataindex)
                        console.log(curr)
                        var AT_index = curr.indexOf('@')
                        var currqty = curr.slice(0, AT_index)
                        var currcolumn = curr.slice(AT_index + 1)

                        var regdate = /^(?:(?!0000)[0-9]{4}-(?:(?:0[1-9]|1[0-2])-(?:0[1-9]|1[0-9]|2[0-8])|(?:0[13-9]|1[0-2])-(?:29|30)|(?:0[13578]|1[02])-31)| {10}(?:[0-9]{2}(?:0[48]|[2468][048]|[13579][26])|(?:0[48]|[2468][048]|[13579][26])00)-02-29)$/
                        if (!regdate.test(currcolumn) && params.value != undefined) {
                            console.log('not date')
                            haserror = true;
                            that.$confirm({
                                title: 'invalid date',
                                content: 'Error bucket:' + currqty + '@' + currcolumn,
                                onOk() {
                                },
                                onCancel() {
                                }
                            })
                        }
                        ;
                        var regdig = /^[0-9]*$/
                        console.log('currqty', currqty)
                        if (!regdig.test(currqty) || currqty.length == 0) {
                            console.log('not int')
                            haserror = true;
                            that.$confirm({
                                title: 'invalid qty',
                                content: 'Error bucket:' + currqty + '@' + currcolumn,
                                onOk() {
                                },
                                onCancel() {
                                }
                            })
                        }
                        changelist.push({
                            'column': currcolumn,
                            'qty': parseInt(currqty),
                            'sorid': currcolumn.replace('-', '').replace('-', '')
                        })
                        newstr = newstr.slice(dataindex + 1)
                        console.log("changeList:",changelist)
                    }
                    //validate if has duplicate bucket will triger notification
                    var duplicate = [];
                    changelist.forEach(item => {
                        console.log('if same duplicate will >1 :', changelist.filter(curr => curr.column == item.column).length)
                        if (changelist.filter(curr => curr.column == item.column).length > 1) {
                            if (duplicate.indexOf(item.column) < 0) {
                                duplicate.push(item.column);
                            }

                        }
                    });
                    if (duplicate.length > 0) {
                        console.log('not date');
                        that.$confirm({
                            title: 'duplicate date',
                            content: 'Error bucket:' + duplicate.toString(),
                            onOk() {
                            },
                            onCancel() {
                            }
                        })
                    } else if (!haserror) {
                        that.shiptoday(changelist, params.data.RID);
                        that.setclosedday(params.data.RID);
                        that.gridApi.redrawRows({rowNodes: this.gridApi.getDisplayedRowAtIndex()});
                    }

                }
                //bucket edit
                if (params.colDef.headerName.indexOf('-') > 0) {
                    if (params.value && params.value != ""&&!NumberUtil.validPositiveInteger(params.value) ) {
                        this.$confirm({
                            title: 'Not Number',
                            content: "Please input Number!",
                            onOk() {
                            },
                            onCancel() {
                            }
                        });
                    } else {
                        //将value值添加到shipping schedule中
                        var currentShipS="";
                        if (params.value){
                            currentShipS=params.value + '@' + params.colDef.headerName;
                        }
                        var shippinglist = [];
                        var newShippingScheduleStr = params.data.SHIPPINGSCHEDULE;
                        // SHIPPING has Value
                        if (params.data.SHIPPINGSCHEDULE) {
                            shippinglist = newShippingScheduleStr.split(",");
                            var sortIndex=0;
                            for (let i = 0; i < shippinglist.length; i++) {
                                var shippinglistElement=shippinglist[i];
                                //存在替换，不存在插入排序
                                if (shippinglistElement.indexOf(params.colDef.headerName) != -1){
                                    shippinglist[i]=currentShipS;
                                    sortIndex=-1;
                                    break;
                                }
                                if (currentShipS!=""){
                                    var date=parseInt(shippinglistElement.split("@")[1].replace(/-/g,""));
                                    var dateNew=parseInt(currentShipS.split("@")[1].replace(/-/g,""));
                                    if (dateNew>date){
                                        sortIndex=i+1;
                                    }else {
                                        sortIndex=i;
                                    }
                                }else{
                                    sortIndex=i+1;
                                }
                            }
                            //替换的不需要走排序插入
                            if (sortIndex!=-1){
                                shippinglist.splice(sortIndex,0,currentShipS);
                            }
                        }else {
                            shippinglist.push(currentShipS)
                        }
                        var str="";
                        let resShippinglist = shippinglist.filter((ship) => {
                            return ship != "";
                        });
                        str=resShippinglist.join(",")
                        for (var editrowindex = 0; editrowindex <= this.rowData.length - 1; editrowindex++) {
                            if (this.rowData[editrowindex].RID == params.data.RID) {
                                this.rowData[editrowindex]['SHIPPINGSCHEDULE'] = str;
                            }
                        }
                        that.gridApi.redrawRows({rowNodes: this.gridApi.getDisplayedRowAtIndex()})
                        this.setclosedday(params.data.RID)
                    }

                }
                // Real Short edit todo 需要将that.setclosedday 提成通用方法
                if (params.colDef.field === "REALSHORTAGE"){
                    that.setclosedday(params.data.RID);
                }
            },

            setclosedday(RID) {
                for (var currindex = 0; currindex <= this.rowData.length - 1; currindex++) {
                    if (this.rowData[currindex].RID === RID) {
                        console.log(this.currentDate)
                        var shortage=this.rowData[currindex].REALSHORTAGE;
                        if (shortage>0){
                            //取本行的qty之和
                            let qtySum=0;
                            for (const day of this.DatetoDay) {
                                var currentDateInt=parseInt(this.currentDate.replace(/-/g,""));
                                var forDateInt=parseInt(day.Date.replace(/-/g,""));
                                //当天之后的才会参与计算
                                if (forDateInt>=currentDateInt){
                                    const dayInt = this.rowData[currindex][day.Day];
                                    if (NumberUtil.validPositiveInteger(dayInt)){
                                        qtySum= qtySum+parseInt(dayInt);
                                        if (qtySum>=shortage){
                                            this.rowData[currindex]['CLOSEDDAY']=day.Date+"";
                                            break;
                                        }
                                    }
                                }
                            }
                            if (qtySum<shortage){
                                this.rowData[currindex]['CLOSEDDAY'] = "";
                            }
                        }else {
                            this.rowData[currindex]['CLOSEDDAY'] = "";
                        }
                        break;

                    }
                }
                this.gridApi.redrawRows({rowNodes: this.gridApi.getDisplayedRowAtIndex()})
            },
            shiptoday(changelist, RID) {
                //                console.log(this.cellDefs);
                var editrowindex
                for (var currindex = 0; currindex <= this.rowData.length - 1; currindex++) {
                    if (this.rowData[currindex].RID == RID) {
                        editrowindex = currindex
                    }
                }
                for (var i = 0; i <= 200; i++) {
                    //                        console.log("D",i)
                    if (this.rowData[editrowindex].hasOwnProperty('D' + i)) {
                        console.log('D', i, this.rowData[editrowindex]['D' + i])
                        this.rowData[editrowindex]['D' + i] = 0
                    }
                }
                changelist.forEach(item => {
                    console.log(item.column, item.qty)
                    var currday = this.DatetoDay.filter(dayitem => dayitem.Date == item.column)[0].Day
                    console.log(currday)
                    this.rowData[editrowindex][currday] = item.qty
                })
            },
            cellEditingStarted() {
                var cellDefs = this.gridApi.getEditingCells()
                this.cellDefs = cellDefs
            },
            rowEditingStarted() {
            },
            PublishBPSClick() {
                var that = this;
                console.log('PublishBPSClick')
                this.form.validateFields((err, values) => {
                    if (!err) {
                        this.queryParam = {}
                        this.queryParam.item = values.item
                        this.queryParam.siteid = values.siteid
                        this.queryParam.bu = values.bu
                        this.queryParam.supplier = values.supplier
                        this.queryParam.PROCITEMGROUP = values.procitemgroup;
                        //                    this.queryParam.plantType = values.plantType;
                        //                        this.getListData();
                    } else {
                        const message = 'Search condition error'
                        const description = 'please input search conditions'
                        that.$message.error(that.$Utils.messageWithClose(message, description))
                    }
                })

                shortagePublish(this.queryParam)
                    .then(res => {
                        if (res.code == 0) {
                            that.$message.success(that.$Utils.messageWithClose('Success', res.msg))
                        }
                        return res
                    }).catch(err => {
                    console.log(err)
                })
            },
            PublishETAClick() {
                console.log('PublishETAClick')
                var that = this
                this.form.validateFields((err, values) => {
                    if (!err) {
                        this.queryParam = {}
                        this.queryParam.item = values.item
                        this.queryParam.siteid = values.siteid
                        this.queryParam.bu = values.bu
                        this.queryParam.supplier = values.supplier
                        this.queryParam.PROCITEMGROUP = values.procitemgroup;
                    } else {
                        const message = 'Search condition error'
                        const description = 'please input search conditions'
                        that.$message.error(that.$Utils.messageWithClose(message, description))
                    }
                })
                etaPublish(this.queryParam)
                    .then(res => {
                        if (res.code == 0) {
                            that.$message.success(that.$Utils.messageWithClose('Success', res.msg))
                        }
                        return res
                    }).catch(err => {
                    console.log(err)
                })
            },
            AddOnClick() {
                console.log('Add click')
                this.addBtn = 'press'
                this.editBtn = 'hide'
                this.submitBtn = 'show'

                this.columnDefs[0].headerName = 'status'
                this.columnDefs[0].field = 'status'
                this.columnDefs[0].width = 120

                // enable edit for allcolumn
                for (var i = 1; i < this.columnDefs.length; i++) {
                    this.columnDefs[i].editable = true
                }
                ;
                this.columnDefs[1].editable = false// disable type
                this.columnDefs[2].editable = false// disable bu
                this.columnDefs[5].editable = false// disable itemgroup
                this.gridApi.setColumnDefs(this.columnDefs)
                // remove currdata
                this.rowData = []
                // add new blank record
                this.rowData.unshift({status: 'new', type: 'ItemNo'})
                //                this.rowData.push(Json.stringify(list));
                // autosize
                var allColumnIds = []
                this.gridColumnApi.getAllColumns().forEach(function (column) {
                    allColumnIds.push(column.colId)
                })
                setTimeout(this.gridColumnApi.autoSizeColumns(allColumnIds, false), 2000)
                // set curr edit row
                this.gridApi.startEditingCell({
                    rowIndex: 0,
                    colKey: 'bu'
                })
            },
            CancelOnClick() {
                var that = this
                this.defaultColDef.floatingFilter = true,
                    this.$confirm({
                        title: 'Cancel',
                        content: 'Are you sure to abandon the modification？',
                        onOk() {
                            console.log('cancel')
                            that.editable = !that.editable
                            that.weekly = false
                            that.monthly = false
                            that.columnGroupShow = 'closed'
                            that.weekhide = true
                            that.monthhide = true
                            that.changelist = []
                            that.columnDefs = []
                            that.spanchangedata = []
                            that.customize()
                        },
                        onCancel() {
                        }
                    });

            },
            SubmitOnClick() {
                var that = this;
                this.defaultColDef.floatingFilter = true,
                console.log('sumbmit');
                var finallist = [];
                //add span data to last
                finallist = this.changelist.concat(this.spanchangedata);
                console.log('final list is:', finallist);

                ETAdynamicUpdate(finallist)
                    .then(res => {
                        if (res.code == 0) {
                            const message = that.$t("lang.messageEditSuccess")
                            const description = res.msg;
                            that.$message.success(that.$Utils.messageWithClose(message, description))
                            this.spanchangedata = []

                            this.editable = !this.editable
                            this.weekly = false
                            this.monthly = false
                            this.columnGroupShow = 'closed'
                            this.weekhide = true
                            this.monthhide = true
                            this.changelist = []
                            this.columnDefs = []
                            this.spanchangedata = []
                            this.customize()
                        } else {
                            const message = that.$t("lang.messageEditFail")
                            const description = res.msg;
                            that.$message.error(that.$Utils.messageWithClose(message, description))
                        }
                    })
                    .catch(er => {
                        const message = that.$t("lang.messageEditFail")
                        const description = res.msg;
                        this.$message.error(this.$Utils.messageWithClose(message, description))
                        console.log(er)
                    })
            },
            filterOption(input, option) {
                return (
                    option.componentOptions.children[0].text
                        .toLowerCase()
                        .indexOf(input.toLowerCase()) >= 0
                );
            },


            setDropDownLists() {
                this.filterList.forEach(element => {
                    if (element['decorator'] == 'item') {
                        element['dropDownList'] = [].concat(this.ETAItemList)
                    } else if (element['decorator'] == 'siteid') {
                        element['dropDownList'] = [].concat(this.ETAsiteIdList)
                    } else if (element['decorator'] == 'bu') {
                        element['dropDownList'] = [].concat(this.ETABUList)
                    } else if (element['decorator'] == 'supplier') {
                        element['dropDownList'] = [].concat(this.ETASupplierList)
                    }
                })
            },
            getDropDown(param, dropdownList, key) {
                getDropDownList(Object.assign({}, param)).then(res => {
                    dropdownList.splice(0)
                    res.result.forEach(el => {
                        dropdownList.push(el[key])
                    })
                })
            },
            handleDropDownChange(value, decorator) {
                console.log('handleDropDownChange', value, decorator);
                if (decorator == 'supplier') {
                    this.querysupplier = value;
                }
            },
            getListData() {
                /***
                 * 调用接口，从数据库查询数据方法
                 * paramters :
                 *  1.pageNum 页数
                 *      不分页，所以设置pageNum:1
                 *  2.pageSize 每页数据量
                 *      ag-grid使用的是假分页，但可以支持100000数据加载到内存，所以设置pageSize:100000
                 */
                this.searchLoading = true
            },
            handleSubmit(e) {
                e.preventDefault()
                this.form.validateFields((err, values) => {
                    console.log('err', err)
                    console.log('values', values)
                    if (!err) {
                        const type = 'error'
                        const message = 'Search condition error'
                        const description = 'please input search conditions'
                        this.openNotificationWithIcon(type, message, description)
                    }
                })
            },
            addNewTable() { // 新建列表
                this.$router.replace('/partsOwner/partsOwner_add')
            },
            editSelectOne() { // 修改选中行
                const selectedRowKeyslen = this.selectedRowKeys.length
                console.log(selectedRowKeyslen)
                if (selectedRowKeyslen == 1) {
                    const editSelectKey = this.selectedRowKeys[0]
                    Vue.ls.set('partsOwner_editSelectKey', editSelectKey)
                    this.$router.replace(`/partsOwner/partsOwner_edit`)
                } else if (selectedRowKeyslen < 1) {
                    const type = 'warning'
                    const message = 'Edit Warning'
                    const description = 'Please Select Edit Row'
                    this.openNotificationWithIcon(type, message, description)
                } else {
                    const type = 'warning'
                    const message = 'Edit Warning'
                    const description = 'Edit Multi Rows'
                    this.openNotificationWithIcon(type, message, description)
                }
            },
            autoDeploy() {
                console.log('auto deploy')
                var ridList = []
                for (var i = 0; i < this.gridApi.getSelectedRows().length; i++) {
                    ridList.push({
                        rid: this.gridApi.getSelectedRows()[i].rid
                    })
                }
                console.log(JSON.stringify(ridList))
                autoRelease(ridList)
                    .then(res => {
                        if (res.code == 0) {
                            this.$notification.open({
                                message: 'Success',
                                description: this.$t('lang.messageEditSuccess'),
                                duration: 6,
                                style: {background: '#52C41A'}
                            })
                            this.$store.dispatch('ToggleCloseTab', '')
                            setTimeout(() => {
                                this.$store.dispatch('ToggleCloseTab', this.$route.path)
                                this.$router.replace(`/partsOwner/partsOwner_list`)
                            }, 500)
                        } else {
                            this.$notification.open({
                                message: 'Error',
                                description: res.msg,
                                duration: 6,
                                style: {background: '#F5222D'}
                                //                                style: { background: "#F5222D" ,},
                                //                                placement:'bottomRight',
                            })
                        }
                        // this.$emit('ok', values)
                    })
                    .catch(er => {
                        this.$message.error(er.msg)
                        console.log(er)
                    })
            },
            replaceOwner() {
                console.log('replaceOwner')
                var loginname = Vue.ls.get('LOGINNAME')
                var ridList = []
                for (var i = 0; i < this.gridApi.getSelectedRows().length; i++) {
                    console.log(this.gridApi.getSelectedRows()[i].rid)
                    ridList.push({
                        itemowner: loginname,
                        rid: this.gridApi.getSelectedRows()[i].rid
                    })
                }

                console.log('selected rid :', ridList)

                //                ridList

                itemOwnerChange(ridList)
                    .then(res => {
                        if (res.code == 0) {
                            this.$notification.open({
                                message: 'Success',
                                description: this.$t('lang.messageEditSuccess'),
                                duration: 6,
                                style: {background: '#52C41A'}
                            })
                            this.$store.dispatch('ToggleCloseTab', '')
                            setTimeout(() => {
                                this.$store.dispatch('ToggleCloseTab', this.$route.path)
                                this.$router.replace(`/partsOwner/partsOwner_list`)
                            }, 500)
                        } else {
                            this.$notification.open({
                                message: 'Error',
                                description: res.msg,
                                duration: 6,
                                style: {background: '#F5222D'}
                            })
                        }
                    })
                    .catch(er => {
                        this.$message.error(er.msg)
                        console.log(er)
                    })
            },
            doubleClickOnRow(record) {
                // 双击行查看详情
                //                const rowKey = record.target.parentNode.dataset.rowKey
                //                console.log(rowKey)
                Vue.ls.set('partsOwner_dblclickRowKey', rowKey)
                this.$router.replace('/partsOwner/partsOwner_detail')
            },
            // 选择列表
            onSelectChange(selectedRowKeys, selectedRows) {
                this.selectedRowKeys = selectedRowKeys
            },
            // 修改用户
            editListFun(rowKey, disab) {
                this.$refs.editForm.edit(rowKey, disab)
            },
            // 删除选中列表
            deleteSeclectAll() {
                var that = this;
                if (this.selectedRowKeys.length == 0) {
                    // this.$message.warning("Please select row(s).");
                    const message = 'Edit Warning'
                    const description = 'Please Select Delete Row'
                    that.$message.warning(that.$Utils.messageWithClose(message, description))
                    return
                }
                const rowKeys = []
                this.selectedRowKeys.forEach(element => {
                    rowKeys.push({
                        rid: element.split('@')[0]
                    })
                })
                this.delfun(rowKeys)
            },
            delfun(rowKeys) {
                const self = this
                this.$confirm({
                    title: self.$t('lang.messageDeleteConfirmTitle'),
                    content: self.$t('lang.messageDeleteSelectedConfirm'),
                    onOk() {
                        return del(rowKeys)
                            .then(res => {
                                //                            console.log(res);
                                if (res.code == '0') {
                                    const type = 'success'
                                    const message = 'Delete Successful'
                                    const description = 'Delete Successful'
                                    self.$message.success(that.$Utils.messageWithClose(message, description))
                                    self.selectedRowKeys = []
                                    self.handleOk() // 删除后刷新列表
                                } else {
                                    const type = 'error'
                                    const message = 'Delete Failed'
                                    const description = res.msg
                                    self.$message.error(that.$Utils.messageWithClose(message, description))
                                }
                            })
                            .catch(err => {
                                console.log(err)
                            })
                    },
                    onCancel() {
                    }
                })
            },
            initbucket() {
                const paramters = {}
                getDateMapping(paramters)
                    .then(res => {
                        console.log('curr time sheet is:', res.result)

                        this.currentDate = res.result.currentDate
                        this.weekendday = res.result['weekenddays']
                        this.monthendday = res.result['monthenddays']
                        this.monthday = res.result['Month2DayMapEntities']
                        this.weekday = res.result['Week2DayMapEntities']
                        return res
                    }).catch(err => {
                    console.log(err)
                })
            },
            // 更改列表数组
            changeLanguage() {
                var user_grp = Vue.ls.get('USER_GROUP')
                var that = this
                this.columnDefs = []
                var monthqty = parseInt(0)
                const paramters = {'uiName': 'ODM_SHORTAGE', 'languageId': this.$store.getters.language}
                ETAstyleList(paramters)
                    .then(res => {
                        var styleList = res.result.styleList
                        that.userAuth = res.result.userAuth
                        var columninfo = styleList.slice(0, 3)
                        columninfo.forEach(item => {
                            //增加NewItem的style
                            if(item.headerName === 'Basic Information'){
                                if (item.children[0].field === 'MISSINGTYPE') {
                                   item.children.splice(0,1)
                                }
                                const newItem={
                                    enablePivot:"200",
                                    headerName:"New Item",
                                    field:"MISSINGTYPE",
                                    isEditable:true,
                                    dataType:"string",
                                    enableRowGroup:"left",
                                    cellStyle: function(params) {
                                        const  styles={
                                                'border-right': '0.25px solid lightgrey !important',
                                                'text-align': 'center'
                                            }
                                        if (params.data.MISSINGTYPE == 'NEW') {
                                            styles.background="#FFE7EF";
                                        }
                                        if (params.data.MISSINGTYPE == 'CHANGE') {
                                            styles.background="#FFECD8";
                                        }
                                        return styles
                                    }
                                }
                                item.children.unshift(newItem)
                            }
                            var childrenindex = 0
                            item.children.forEach(childrenitem => {
                                if (childrenitem.field == 'PROCITEMGROUP') {
                                    item.children[childrenindex].width = 250
                                }
                                if (childrenitem.isEditable) {
                                    item.children[childrenindex].editable = this.editable
                                }
                                if (childrenitem.cellEditor == 'agRichSelectCellEditor') {
                                    item.children[childrenindex].cellEditorParams = JSON.parse(childrenitem.cellEditorParams)
                                }

                                if (this.spancolumn.includes(childrenitem.field)) { // 要合并单元格
                                    item.children[childrenindex].cellStyle = function (params) {
                                        var spandata = that.spanrowdata.filter(item => item.rid == params.data.RID)
                                        if (spandata.length > 0) {
                                            if (spandata[0].count > 1) {
                                                let height = (28 * spandata[0].count - 2) + 'px !important'
                                                return {
                                                    'height': height,
                                                    'background': '#fff',
                                                    'align-items': 'center',
                                                    'display': 'flex',
                                                    'white-space': 'pre-wrap',
                                                    'border-right': '0.25px solid lightgrey !important',
                                                    // 'border-bottom': '0.25px solid lightgrey !important',
                                                    'line-height': '12px',
                                                    'vertical-align': 'middle',
                                                    'color': '#000'
                                                }
                                            } else {
                                                return {
                                                    'background': '#fff',
                                                    'align-items': 'center',
                                                    'display': 'flex',
                                                    'white-space': 'pre-wrap',
                                                    'border-right': '0.25px solid lightgrey !important',
                                                    'line-height': '12px',
                                                    'vertical-align': 'middle',
                                                    'color': '#000'
                                                }
                                            }
                                        }
                                    }
                                    item.children[childrenindex].rowSpan = function (params) {
                                        var spandata = that.spanrowdata.filter(item => item.rid == params.data.RID)
                                        if (spandata.length > 0) {
                                            if (spandata[0].count > 1) {
                                                return spandata[0].count
                                            }
                                        } else {
                                            return 1
                                        }
                                    }

                                } else { // 不合并单元格
                                    if ( item.children[childrenindex].cellStyle){
                                        item.children[childrenindex].cellStyle['border-right'] = '0.25px solid lightgrey !important'
                                    }else{
                                        item.children[childrenindex].cellStyle = {
                                            'border-right': '0.25px solid lightgrey !important',
                                        }
                                    }
                                }
                                childrenindex = childrenindex + 1
                            })
                            this.columnDefs.push(item)
                        })
                        var bucket = styleList.slice(3)
                        var weekly_bucket = []
                        var month_bucket = []

                        bucket.forEach(currcol => {
                            this.DatetoDay.push({
                                'Day': currcol.field.toString(),
                                'Date': currcol.headerName.toString()
                            })
                            if (this.weekendday.indexOf(currcol.field.toString()) >= 0 && !this.monthly || currcol.field.toString() == 'D210') {
                                if (this.weekendday.indexOf(currcol.field.toString()) >= 0 && !this.monthly) {
                                    currcol.cellStyle = {
                                        backgroundColor: '#e3fbea',
                                        color: '#000000',
                                        'text-align': 'center'
                                    }
                                }
                                ;

                                currcol.editable = this.editable
                                currcol.columnGroupShow = this.columnGroupShow
                                currcol.hide = that.dayhide
                                if (!this.monthly) {
                                    weekly_bucket.push(currcol)
                                }

                                var weekindex = this.weekday.findIndex(item => item.startDate == currcol.field.toString())
                                var daylist = this.weekday.filter(item => item.week == this.weekday[weekindex].week)
                                var startday = daylist[0].startDate
                                var endday = daylist[daylist.length - 1].startDate
                                var startdate = this.DatetoDay.filter(item => item.Day == startday)[0].Date
                                var enddate = this.DatetoDay.filter(item => item.Day == endday)[0].Date

                                if (currcol.headerName < that.currentDate) {
                                    weekly_bucket.push({
                                        headerName: startdate + '/' + enddate,
                                        colId: this.weekday[weekindex].week,
                                        width: 200,
                                        cellStyle: {
                                            backgroundColor: '#f2f2f2',
                                            color: '#000000',
                                            'text-align': 'center'
                                        },
                                        hide: this.weekhide,
                                        valueGetter: function (params) {
                                            var result = parseInt(0)
                                            var colval = parseInt(0)
                                            // sum weekday
                                            daylist.forEach(day => {
                                                var currcol = day.startDate

                                                var day1 = params.getValue(currcol)
                                                var day2 = params.getValue(currcol + '_1')

                                                if (day1 != null && day1 != undefined && day1 != "" && day1 != "NaN") {
                                                    colval = day1
                                                } else if (day2 != null && day2 != undefined && day1 != "" && day1 != "NaN") {
                                                    colval = day2
                                                } else {
                                                    colval = 0
                                                }

                                                var regdig = /^[0-9]*$/
                                                if (!regdig.test(day1) || day1.length == 0) {
                                                    console.log('not int')
                                                } else {
                                                    result = parseInt(result) + parseInt(colval)
                                                }

                                            })
                                            return result
                                        }
                                    });
                                    if (this.weekendday.indexOf(currcol.field.toString()) >= 0 || currcol.field.toString() == 'D210') {
                                        console.log('past date week end', this.weekday[weekindex].week)
                                        that.columnDefs.push({
                                            headerName: this.weekday[weekindex].week,
                                            groupId: this.weekday[weekindex].week,
                                            children: weekly_bucket,
                                        });
                                        weekly_bucket = [];
                                    }
                                } else {
                                    weekly_bucket.push({
                                        headerName: startdate + '/' + enddate,
                                        colId: this.weekday[weekindex].week,
                                        width: 200,
                                        hide: this.weekhide,
                                        valueGetter: function (params) {
                                            var result = parseInt(0)
                                            var colval = parseInt(0)
                                            // sum weekday
                                            daylist.forEach(day => {
                                                var currcol = day.startDate

                                                var day1 = params.getValue(currcol)
                                                var day2 = params.getValue(currcol + '_1')
                                                if (day1 != null && day1 != undefined && day1 != "") {
                                                    colval = day1;
                                                } else if (day2 != null && day2 != undefined && day2 != "") {
                                                    colval = day2;
                                                } else {
                                                    colval = 0
                                                }
                                                var regdig = /^[0-9]*$/
                                                if (!regdig.test(day1) || day1.length == 0) {
                                                } else {
                                                    result = parseInt(result) + parseInt(colval)
                                                }
                                            })
                                            return result
                                        }
                                    })
                                    if (this.weekendday.indexOf(currcol.field.toString()) >= 0 || currcol.field.toString() == 'D210') {
//                                        console.log(this.weekday[weekindex].week)
                                        that.columnDefs.push({
                                            headerName: this.weekday[weekindex].week,
                                            groupId: this.weekday[weekindex].week,
                                            children: weekly_bucket
                                        })
                                        //                                    console.log(weekly_bucket)
                                        weekly_bucket = []
                                    }
                                }

                                //whole week bucket push to columndefs


                            }
                            // monthend day bucket push to columndefs
                            if (this.monthendday.indexOf(currcol.field.toString()) >= 0 && !this.weekly) {
                                currcol.editable = this.editable
                                //                                        console.log(currcol.headerName,this.columnGroupShow);
                                currcol.columnGroupShow = this.columnGroupShow

                                //                                    console.log('month hide',this.monthhide)
                                if (!this.monthhide && !this.editable) {
                                    console.log('month end day push', currcol.headerName)
                                    currcol.hide = that.monthhide
                                    month_bucket.push(currcol)
                                }

                                if (!this.dayhide && !this.monthly && this.weekendday.indexOf(currcol.field.toString()) < 0) {
                                    currcol.hide = that.dayhide
                                    weekly_bucket.push(currcol)
                                }

                                // month bucket push to columndefs
                                var currmonth = this.monthday.filter(item => item.startDate == currcol.field.toString())[0]
                                var currfilter = currmonth.month
                                var currmonthlabel = currmonth.monthTitle

                                var monthdaylist = this.monthday.filter(item => item.month == currfilter)
                                if (currcol.headerName < that.currentDate) {
                                    month_bucket.push({
                                        headerName: currfilter,
                                        groupId: currfilter,
                                        colId: currfilter,
                                        hide: that.monthhide,
                                        cellstyle: {
                                            backgroundColor: '#f2f2f2',
                                            color: '#000000',
                                            'text-align': 'center'
                                        },
                                        valueGetter: function (params) {
                                            var result = parseInt(0)
                                            var colval = parseInt(0)
                                            // sum weekday
                                            monthdaylist.forEach(day => {
                                                var currcol = day.startDate.toString()
                                                var day1 = params.getValue(currcol)
                                                var day2 = params.getValue(currcol + '_1')
                                                //                                                    console.log('day1',day1,'  day2:',day2);
                                                if (day1 != null && day1 != undefined && day1 != "") {
                                                    colval = day1
                                                } else if (day2 != null && day2 != undefined && day2 != "") {
                                                    colval = day2
                                                } else {
                                                    colval = 0
                                                }
                                                var regdig = /^[0-9]*$/
                                                if (!regdig.test(day1) || day1.length == 0) {
                                                    console.log('not int')
                                                } else {
                                                    result = parseInt(result) + parseInt(colval)
                                                }
                                            })
                                            return result
                                        }
                                    })
                                } else {
                                    month_bucket.push({
                                        headerName: currfilter,
                                        groupId: currfilter,
                                        colId: currfilter,
                                        hide: that.monthhide,
                                        valueGetter: function (params) {
                                            var result = parseInt(0)
                                            var colval = parseInt(0)
                                            // sum weekday
                                            monthdaylist.forEach(day => {
                                                var currcol = day.startDate.toString()
                                                var day1 = params.getValue(currcol)
                                                var day2 = params.getValue(currcol + '_1')
                                                //                                                    console.log('day1',day1,'  day2:',day2);
                                                if (day1 != null && day1 != undefined && day1 != "") {
                                                    colval = day1
                                                } else if (day2 != null && day2 != undefined && day2 != "") {
                                                    colval = day2
                                                } else {
                                                    colval = 0
                                                }
                                                var regdig = /^[0-9]*$/
                                                if (!regdig.test(day1) || day1.length == 0) {
                                                    console.log('not int')
                                                } else {
                                                    result = parseInt(result) + parseInt(colval)
                                                }
                                            })
                                            return result
                                        }
                                    })
                                }

                                if (this.monthendday.indexOf(currcol.field.toString()) >= 0) {
                                    that.columnDefs.push({
                                        headerName: currmonthlabel,
                                        children: month_bucket
                                    })
                                    month_bucket = []
                                }

                            }

                            else {
                                //past day
                                if (currcol.headerName < this.currentDate) {
                                    currcol.cellStyle = {
                                        backgroundColor: '#f2f2f2',
                                        color: '#000000',
                                        'text-align': 'center'
                                    }
                                    currcol.editable = this.editable
                                    currcol.columnGroupShow = this.columnGroupShow
                                    if (!this.monthhide && !this.editable) {
                                        currcol.hide = this.monthhide
                                        month_bucket.push(currcol)
                                    }

                                    if (!this.dayhide && this.weekendday.indexOf(currcol.field.toString()) < 0) {
                                        currcol.hide = this.dayhide
                                        weekly_bucket.push(currcol)
                                    }
                                } else {
                                    // future day
                                    currcol.editable = this.editable
                                    currcol.columnGroupShow = this.columnGroupShow
                                    if (!this.monthhide && !this.editable) {
                                        currcol.hide = this.monthhide

                                        if (this.weekendday.indexOf(currcol.field.toString()) >= 0) {
                                            //                                  console.log('weekday:',this.weekendday);
                                            currcol.cellStyle = {
                                                backgroundColor: '#e3fbea',
                                                color: '#000000',
                                                'text-align': 'center'
                                            }
                                        }
                                        ;
                                        month_bucket.push(currcol)
                                    }
                                    if (!this.dayhide && this.weekendday.indexOf(currcol.field.toString()) < 0) {
                                        currcol.hide = this.dayhide
                                        weekly_bucket.push(currcol)
                                    }

                                }
                            }
                        })
                        this.gridApi.setColumnDefs(that.columnDefs)
                        return res
                    }).catch(err => {
                    console.log(err)
                })

                // get filter list
                const paramters2 = {'uiName': 'ODM_SHORTAGE', 'languageId': this.$store.getters.language}
                filterList(paramters2)
                    .then(res => {
                        this.filterList = res.result
                        this.filterList[4].dropDownList = null
                        console.log('curr filter list is:', this.filterList)
                        this.setDropDownLists()
                        return res
                    }).catch(err => {
                    console.log(err)
                })

            },
            // 刷新列表
            handleOk() {
                this.getListData()
            },
            // 收起展开
            toggleAdvanced() {
                this.advanced = !this.advanced
            },
            // 重置
            resetSearchForm() {
                this.queryParam = {
                    date: moment(new Date())
                }
            },
            onBtExport() {

                let params = {'eventName': 'UPLOAD_BS_ORDERSHORTAGE'}
                this.form.validateFields((err, values) => {
                    if (!err) {
                        if (values.bu !== undefined && values.bu.length != 0) {
                            params = {...params, 'BU': values.bu}
                        }
                        if (values.item !== undefined && values.item != '') {
                            params = {...params, 'ITEM': values.item}
                        }
                        if (values.siteid !== undefined && values.siteid != '') {
                            params = {...params, 'SITEID': values.siteid}
                        }
                        if (values.supplier !== undefined && values.supplier != '') {
                            params = {...params, 'SUPPLIERID': values.supplier}
                        }
                        if (values.procitemgroup !== undefined && values.procitemgroup != '') {
                            params = {...params, 'PROCITEMGROUP': values.procitemgroup}
                        }

                    }
                    ;
                })
                console.log(params);
                let url = "common/exportExcel";
                exportByURL(params, url);
            },
            openNotificationWithIcon(type, message, description) {
                //                console.log('open notice')
                //                console.log(window.width)
                this.$notification[type]({
                    message: message,
                    description: description
                    //                    placement:'bottomRight',
                    //                    bottom:'20px',
                })
            },
            getHeight() {
                this.agStyle = 'width: 100%; height:' + parseInt(window.innerHeight * 0.58) + 'px'
            },

            saveFilterOnClicked() {
                this.form.validateFields((err, values) => {
                    if (!err) {
                        if (hasSearchFilters(values)) {
                            this.queryParam.materialGroup = values.materialGroup
                            this.$store.dispatch('ToggleShowNamedModal', {
                                boolean: true,
                                queryParam: this.queryParam
                            })
                        } else {
                            const type = 'warning'
                            const message = 'Save condition warning'
                            const description = 'please enter at least one filter'
                            this.openNotificationWithIcon(type, message, description)
                        }
                    }
                })
            },

            // 开启、关闭选择框
            tableOption() {
                if (!this.optionAlertShow) {
                    this.options = {
                        alert: {
                            show: true, clear: () => {
                                this.selectedRowKeys = []
                            }
                        },
                        rowSelection: {
                            selectedRowKeys: this.selectedRowKeys,
                            onChange: this.onSelectChange
                        }
                    }
                    this.optionAlertShow = true
                } else {
                    this.options = {
                        alert: false,
                        rowSelection: null
                    }
                    this.optionAlertShow = false
                }
            }
            //
        },
        destroyed() {
            window.removeEventListener('resize', this.getHeight)
        }
    }
</script>

<style scoped>

</style>
