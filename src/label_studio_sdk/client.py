# This file was auto-generated by Fern from our API Definition.

import os
import typing

import httpx

from .actions.client import ActionsClient, AsyncActionsClient
from .annotations.client import AnnotationsClient, AsyncAnnotationsClient
from .core.api_error import ApiError
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .data.client import AsyncDataClient, DataClient
from .data_manager.client import AsyncDataManagerClient, DataManagerClient
from .environment import LabelStudioEnvironment
from .export_storage.client import AsyncExportStorageClient, ExportStorageClient
from .import_storage.client import AsyncImportStorageClient, ImportStorageClient
from .labels.client import AsyncLabelsClient, LabelsClient
from .machine_learning.client import AsyncMachineLearningClient, MachineLearningClient
from .ml.client import AsyncMlClient, MlClient
from .organizations.client import AsyncOrganizationsClient, OrganizationsClient
from .predictions.client import AsyncPredictionsClient, PredictionsClient
from .projects.client import AsyncProjectsClient, ProjectsClient
from .tasks.client import AsyncTasksClient, TasksClient
from .users.client import AsyncUsersClient, UsersClient
from .views.client import AsyncViewsClient, ViewsClient
from .webhooks.client import AsyncWebhooksClient, WebhooksClient


class LabelStudio:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : LabelStudioEnvironment
        The environment to use for requests from the client. from .environment import LabelStudioEnvironment



        Defaults to LabelStudioEnvironment.DEFAULT



    api_key : typing.Optional[str]
    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests by default the timeout is 60 seconds, unless a custom httpx client is used, in which case a default is not set.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.Client]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    Examples
    --------
    from label_studio_sdk.client import LabelStudio

    client = LabelStudio(
        api_key="YOUR_API_KEY",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: LabelStudioEnvironment = LabelStudioEnvironment.DEFAULT,
        api_key: typing.Optional[str] = os.getenv("LABEL_STUDIO_API_KEY"),
        timeout: typing.Optional[float] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.Client] = None
    ):
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        if api_key is None:
            raise ApiError(
                body="The client must be instantiated be either passing in api_key or setting LABEL_STUDIO_API_KEY"
            )
        self._client_wrapper = SyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            api_key=api_key,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.Client(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.Client(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
        )
        self.annotations = AnnotationsClient(client_wrapper=self._client_wrapper)
        self.users = UsersClient(client_wrapper=self._client_wrapper)
        self.actions = ActionsClient(client_wrapper=self._client_wrapper)
        self.data_manager = DataManagerClient(client_wrapper=self._client_wrapper)
        self.views = ViewsClient(client_wrapper=self._client_wrapper)
        self.projects = ProjectsClient(client_wrapper=self._client_wrapper)
        self.organizations = OrganizationsClient(client_wrapper=self._client_wrapper)
        self.labels = LabelsClient(client_wrapper=self._client_wrapper)
        self.ml = MlClient(client_wrapper=self._client_wrapper)
        self.machine_learning = MachineLearningClient(client_wrapper=self._client_wrapper)
        self.predictions = PredictionsClient(client_wrapper=self._client_wrapper)
        self.tasks = TasksClient(client_wrapper=self._client_wrapper)
        self.import_storage = ImportStorageClient(client_wrapper=self._client_wrapper)
        self.export_storage = ExportStorageClient(client_wrapper=self._client_wrapper)
        self.webhooks = WebhooksClient(client_wrapper=self._client_wrapper)
        self.data = DataClient(client_wrapper=self._client_wrapper)


class AsyncLabelStudio:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : LabelStudioEnvironment
        The environment to use for requests from the client. from .environment import LabelStudioEnvironment



        Defaults to LabelStudioEnvironment.DEFAULT



    api_key : typing.Optional[str]
    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests by default the timeout is 60 seconds, unless a custom httpx client is used, in which case a default is not set.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.AsyncClient]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    Examples
    --------
    from label_studio_sdk.client import AsyncLabelStudio

    client = AsyncLabelStudio(
        api_key="YOUR_API_KEY",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: LabelStudioEnvironment = LabelStudioEnvironment.DEFAULT,
        api_key: typing.Optional[str] = os.getenv("LABEL_STUDIO_API_KEY"),
        timeout: typing.Optional[float] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.AsyncClient] = None
    ):
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        if api_key is None:
            raise ApiError(
                body="The client must be instantiated be either passing in api_key or setting LABEL_STUDIO_API_KEY"
            )
        self._client_wrapper = AsyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            api_key=api_key,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.AsyncClient(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.AsyncClient(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
        )
        self.annotations = AsyncAnnotationsClient(client_wrapper=self._client_wrapper)
        self.users = AsyncUsersClient(client_wrapper=self._client_wrapper)
        self.actions = AsyncActionsClient(client_wrapper=self._client_wrapper)
        self.data_manager = AsyncDataManagerClient(client_wrapper=self._client_wrapper)
        self.views = AsyncViewsClient(client_wrapper=self._client_wrapper)
        self.projects = AsyncProjectsClient(client_wrapper=self._client_wrapper)
        self.organizations = AsyncOrganizationsClient(client_wrapper=self._client_wrapper)
        self.labels = AsyncLabelsClient(client_wrapper=self._client_wrapper)
        self.ml = AsyncMlClient(client_wrapper=self._client_wrapper)
        self.machine_learning = AsyncMachineLearningClient(client_wrapper=self._client_wrapper)
        self.predictions = AsyncPredictionsClient(client_wrapper=self._client_wrapper)
        self.tasks = AsyncTasksClient(client_wrapper=self._client_wrapper)
        self.import_storage = AsyncImportStorageClient(client_wrapper=self._client_wrapper)
        self.export_storage = AsyncExportStorageClient(client_wrapper=self._client_wrapper)
        self.webhooks = AsyncWebhooksClient(client_wrapper=self._client_wrapper)
        self.data = AsyncDataClient(client_wrapper=self._client_wrapper)


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: LabelStudioEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
