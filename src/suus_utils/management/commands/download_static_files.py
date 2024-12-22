from dataclasses import dataclass
from pathlib import Path
from typing import Any, List

from django.conf import settings
from django.core.management.base import BaseCommand

from suus_utils.downloader import download_to_local


@dataclass
class DownloadInfo:
    filename: str
    url: str
    path: Path


FILES_TO_DOWNLOAD: List[DownloadInfo] = [
    DownloadInfo(
        filename="htmx.min.js",
        url="https://unpkg.com/htmx.org@2.0.2",
        path=settings.STATICFILES_VENDOR_DIR,
    ),
]


class Command(BaseCommand):

    def handle(self, *args: Any, **options: Any):
        self.stdout.write("Downloading vendor static files")
        completed_downloads = []
        for download_info in FILES_TO_DOWNLOAD:
            path = download_info.path / download_info.filename
            dl_success = download_to_local(download_info.url, path)
            if dl_success:
                completed_downloads.append(download_info)
            else:
                self.stdout.write(
                    self.style.ERROR(f"Failed to download {download_info.url}")
                )
        if len(FILES_TO_DOWNLOAD) == len(completed_downloads):
            self.stdout.write(
                self.style.SUCCESS("Successfully updated all vendor static files.")
            )
        else:
            self.stdout.write(self.style.WARNING("Some files were not updated."))
